from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from block_inventory.forms import BlockForm
from block_inventory.helpers import find_block
from block_inventory.models import Blocks, db
from playsound import playsound
# from block_inventory.models import Drone, db
import time




site = Blueprint('site', __name__, template_folder = 'site_templates')

"""
Note that in the above code, some arguments are specified when creating the 
Blueprint object. The first argument, 'site', is the Blueprint's name, this is used
by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name,
which Flask uses to locate the Blueprint's resources
"""


@site.route('/')
def home():
    time.sleep(1)
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.signin'))
    return render_template('index.html')


@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.signin'))
    time.sleep(0.3)
    
    c_block = request.args.get('c_block')
    mcd_block = ''
    user_token = current_user.token
    blocks = Blocks.query.filter_by(user_token = user_token)

    form = BlockForm()
    
    try:
        if request.method == "POST" and form.validate_on_submit():
            
            user_block = form.block.data
            mcd_block = find_block(user_block.title())
            block_texture = f"../../static/images/block/{mcd_block['name']}.png"

            if mcd_block:
                for i in blocks:
                    if mcd_block['id'] == i.mc_id:
                        block = i
                        return render_template('profile.html', form=form, mcd_block=mcd_block, block_texture=block_texture, blocks=blocks, block=block)
            
            mc_id = mcd_block['id']
            name = mcd_block['name']
            displayName = mcd_block['displayName']
            hardness = mcd_block['hardness']
            resistance = mcd_block['resistance']
            stackSize = mcd_block['stackSize']
            diggable = mcd_block['diggable']
            transparent = mcd_block['transparent']
            user_token = current_user.token
            
            block = Blocks(mc_id, name, displayName, hardness, resistance, stackSize, diggable, transparent, user_token)
            
            db.session.add(block)
            db.session.commit()
                 
            blocks = Blocks.query.filter_by(user_token = user_token)

            return render_template('profile.html', form=form, mcd_block=mcd_block, block_texture=block_texture, blocks=blocks, block=block)
    except:
        flash('That block was not found, please check the wording / spelling and try again', 'auth-success')
        playsound("block_inventory/static/sounds/oof_sound.mp3")

    if c_block:
        block = Blocks.query.filter_by(id=c_block).first()
        mcd_block = find_block(block.name)
        block_texture = f"../../static/images/block/{mcd_block['name']}.png"

        return render_template('profile.html', form=form, mcd_block=mcd_block, block_texture=block_texture, blocks=blocks, block=block)

    return render_template('profile.html', form=form, blocks = blocks)


@site.route('/build', methods = ['GET', 'POST'])
def build():
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('auth.signin'))
    time.sleep(0.3)

    user_token = current_user.token
    blocks = Blocks.query.filter_by(user_token = user_token)

    return render_template('build.html', blocks=blocks)

@site.route('/delete_block/<block_id>', methods=['POST'])
@login_required
def delete_block(block_id):
    time.sleep(0.3)
    block = Blocks.query.get(block_id)
    db.session.delete(block)
    db.session.commit()
    return redirect(url_for('site.profile'))