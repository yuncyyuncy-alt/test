import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
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

    if not files or all(f.filename == '' for f in files):
        flash('업로드할 파일을 선택하세요.')
        print('upload error : 파일들이 없거나 파일명에 오류가 있습니다')
        return redirect(url_for('nctodb.nctodb'))

    print('upload', [f.filename for f in files])
    return redirect(url_for('nclist.nclist'))