import functools, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from netcdfweb.db import get_db

from .nclist import bp as nclist_bp

bp = Blueprint('nctodb', __name__, url_prefix='/nctodb')

@bp.route('/')
def nctodb():
    print('nctodb')
    return render_template('nctodb.html')

@bp.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('file')
    print('불러온 파일들 : ', files)

    if not files or all(not f.filename.strip() for f in files) :
        flash('업로드할 파일을 선택하세요.')
        print('upload error : 파일들이 없거나 파일명에 오류가 있습니다')
        return redirect(url_for('nctodb.nctodb'))
    
    for file in files:
        if not file.filename.lower().endswith('.nc'):
            continue
    
        safe_name = os.path.basename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], safe_name))

    print('upload', [f.filename for f in files])
    return redirect(url_for('nclist.nclist'))


    
