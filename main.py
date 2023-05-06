from calculator import *
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from os import path

app = Flask(__name__)
app.config["CLIENT_REPORTS"] = r"static\reports"

"results = None"
structure = None
quality_of_information = False
id = 1
idClient = 0
risk_reliability = []


@app.route('/download', methods=['GET'])
def download_file():
    directory = path.join(app.root_path, app.config["CLIENT_REPORTS"])
    return send_from_directory(directory=directory, path="report.docx", as_attachment=True)
    #return send_from_directory(directory=directory, filename="report.docx")


"""
@app.route('/test_api', methods=['GET'])
def test_api():
    oldImage = "images/figure.png"
    oldReport = "reports/report.docx"

    if os.path.isfile(oldImage):
        os.remove(oldImage)

    if os.path.isfile(oldReport):
        os.remove(oldReport)

    # создание графика
    fig = plt.figure()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # в список Y записываешь сами результаты оценки рисков, на графике самостоятельно выведется шкала на оси Y

    y = [0.067, 0.020, 0.020, 0.020, 0.015, 0.026, 0.062, 0.027, 0.186]

    plt.bar(x, y)
    plt.xticks(x, ['1', '2', '3', '4', '5', '6', '7', '8', 'За все \n действия'])

    plt.show()
    fig.savefig('images/figure.png', dpi=100)

    # создание репорта

    # создание документа
    report = Document()

    # задаем стиль текста по умолчанию
    style = report.styles['Normal']
    # название шрифта
    style.font.name = 'Times New Roman'
    # размер шрифта
    style.font.size = Pt(14)

    # добавление заголовка
    head = report.add_paragraph('ОЦЕНКА РИСКОВ \n')
    # выравнивание заголовка посередине
    head.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # добавление параграф
    report.add_paragraph('Оценка рисков \n')

    # добавить картинку
    picture = report.add_picture('images/figure.png')

    # сохранить репорт
    report.save('reports/report.docx')

    return render_template('index.html')
"""


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/decision-management-process', methods=['GET'])
def decision_management_process():
    global structure
    global id
    global idClient

    structure = None
    id = 1
    idClient = id
    clear_parameters()

    return render_template('management-process.html', structure = structure)

    """results=results"""


@app.route('/decision-management-process/risk', methods=['GET'])
def decision_management_process_risk():
    # return render_template('management-process.html', structure = structure)
    return render_template('management-process.html')


"""
@app.route('/calculator', methods=['POST'])
def calculator():
    if 'number-1' in request.form and 'number-2' in request.form:
        number1 = int(request.form.get('number-1'))
        number2 = int(request.form.get('number-2'))
        global results
        results = number1 + number2


        return redirect(url_for('decision_management_process'))

    else:
        return render_template('management-process.html', results=results)

"""


@app.route('/decision-management-process/reliability-risk', methods=['GET'])
def decision_reliability_risk():
    return render_template('management-process-decision-reliability-risk.html', idClient = idClient)


@app.route('/decision-management-process/requirements-risk', methods=['GET'])
def decision_requirements_risk():

    return render_template('management-process-decision-requirements-risk.html', idClient=idClient, id = id)


@app.route('/decision-management-process/next-1', methods=['POST'])
def next_1():
    if 'quality-of-information' in request.form:
        global quality_of_information
        quality_of_information = request.form.get("quality-of-information")

    if 'structure' in request.form:
        global structure
        structure = request.form.get('structure')

        if structure == "simple":
            # return redirect(url_for('decision_management_process_risk'))
            return redirect(url_for('decision_reliability_risk'))

        else:
            return redirect(url_for('decision_reliability_risk'))

            # return redirect(url_for('decision_management_process'))

    else:
        return redirect(url_for('decision_management_process'))


# Для риска надежности


@app.route('/decision-management-process/next-3', methods=['POST'])
def calc_risk_reliability_next():
    global id
    global idClient
    global risk_reliability

    #id = id + 1
    #idClient = id

    alfa = request.form.get('alfa')
    beta = request.form.get('beta')
    Tmesh = request.form.get('Tmesh')
    Tdiag = request.form.get('Tdiag')
    Tvost = request.form.get('Tvost')
    Tzad = request.form.get('Tzad')

    alfaTime = request.form.get('alfaTime')
    betaTime = request.form.get('betaTime')
    TmeshTime = request.form.get('TmeshTime')
    TdiagTime = request.form.get('TdiagTime')
    TvostTime = request.form.get('TvostTime')
    TzadTime = request.form.get('TzadTime')

    add_parameters_for_reliability(alfa, beta, Tmesh, Tdiag, Tvost, Tzad, alfaTime, betaTime, TmeshTime, TdiagTime,
                                   TvostTime, TzadTime)
    risk_reliability = start_calc_reliability_risk()

    create_report_reliability()
    clear_parameters()
    id = 1
    return redirect(url_for('decision_requirements_risk'))
  #  return render_template('management-process-decision-requirements-risk.html', idClient = idClient)
  #  return redirect(url_for('test_risk'))


@app.route('/decision-management-process/add-3', methods=['POST'])
def calc_risk_reliability_add():
    global id
    global idClient
    global risk_reliability

    id = id + 1
    idClient = id

    alfa = request.form.get('alfa')
    beta = request.form.get('beta')
    Tmesh = request.form.get('Tmesh')
    Tdiag = request.form.get('Tdiag')
    Tvost = request.form.get('Tvost')
    Tzad = request.form.get('Tzad')

    alfaTime = request.form.get('alfaTime')
    betaTime = request.form.get('betaTime')
    TmeshTime = request.form.get('TmeshTime')
    TdiagTime = request.form.get('TdiagTime')
    TvostTime = request.form.get('TvostTime')
    TzadTime = request.form.get('TzadTime')

    add_parameters_for_reliability(alfa, beta, Tmesh, Tdiag, Tvost, Tzad, alfaTime, betaTime, TmeshTime, TdiagTime,
                                   TvostTime, TzadTime)
    risk_reliability = start_calc_reliability_risk()
    return redirect(url_for("decision_reliability_risk"))
    # return render_template('management-process-decision-reliability-risk.html', idClient = idClient)


# Для риска нарушения требований


@app.route('/decision-management-process/next-4', methods=['POST'])
def calc_risk_requirements_next():
    global id
    global idClient
    global risk_reliability

    #id = id + 1
    #idClient = id

    alfa = request.form.get('alfa')
    beta = request.form.get('beta')
    Tmesh = request.form.get('Tmesh')
    Tdiag = request.form.get('Tdiag')
    Tvost = request.form.get('Tvost')
    Tzad = request.form.get('Tzad')

    alfaTime = request.form.get('alfaTime')
    betaTime = request.form.get('betaTime')
    TmeshTime = request.form.get('TmeshTime')
    TdiagTime = request.form.get('TdiagTime')
    TvostTime = request.form.get('TvostTime')
    TzadTime = request.form.get('TzadTime')

    add_parameters_for_reliability(alfa, beta, Tmesh, Tdiag, Tvost, Tzad, alfaTime, betaTime, TmeshTime, TdiagTime,
                                   TvostTime, TzadTime)
    risk_reliability = start_calc_requirements_risk()

    add_report_requirements()
    add_integral_risk()
    return redirect(url_for('test_risk'))
  #  return render_template('management-process-decision-requirements-risk.html', idClient = idClient)
  #  return redirect(url_for('test_risk'))


@app.route('/decision-management-process/add-4', methods=['POST'])
def calc_risk_requirements_add():
    global id
    global idClient
    global risk_reliability

    id = id + 1
  #  idClient = id

    alfa = request.form.get('alfa')
    beta = request.form.get('beta')
    Tmesh = request.form.get('Tmesh')
    Tdiag = request.form.get('Tdiag')
    Tvost = request.form.get('Tvost')
    Tzad = request.form.get('Tzad')

    alfaTime = request.form.get('alfaTime')
    betaTime = request.form.get('betaTime')
    TmeshTime = request.form.get('TmeshTime')
    TdiagTime = request.form.get('TdiagTime')
    TvostTime = request.form.get('TvostTime')
    TzadTime = request.form.get('TzadTime')

    add_parameters_for_reliability(alfa, beta, Tmesh, Tdiag, Tvost, Tzad, alfaTime, betaTime, TmeshTime, TdiagTime,
                                   TvostTime, TzadTime)
    risk_reliability = start_calc_requirements_risk()
    return redirect(url_for("decision_requirements_risk"))
  #  return redirect(url_for("decision_reliability_risk"))


@app.route('/decision-management-process/results', methods=['GET'])
def test_risk():
    return render_template('test-risk.html', risk_reliability = risk_reliability)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


app.run()
