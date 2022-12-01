from flask import Blueprint, render_template, request, redirect, url_for
import requests
from funcoes import Funcoes

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
def formListaFuncionario():
    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if (response.status_code != 200):
                raise Exception(result)
        return render_template('formListaFuncionario.html', result=result)
    except Exception as e:
            return render_template('formListaFuncionario.html', erro=e)

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
def formFuncionario(): 
    return render_template('formFuncionario.html') 