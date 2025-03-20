from flask import Flask, request, jsonify

app = Flask(__name__)

professores = []
alunos = []
turmas = []
