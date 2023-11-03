from flask import Flask, redirect, render_template, request, url_for
import subprocess
import os
abs_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home(text_area="",
         input_fields="",
         output=""):
    if request.method == "POST":
        with open(f'{abs_path}/c_script.c', "w") as the_file:
            script = request.form['coding_area']
            script_inputs = request.form['input_area']
            if script:
                the_file.write(request.form['coding_area'])
                subprocess.Popen(["gcc", "c_script.c", "-o", "c_script.exe"],
                                 text=True,)
                run_file = subprocess.run(["c_script.exe"],
                                          text=True,
                                          input=script_inputs,
                                          capture_output=True,)
                file_output = run_file.stdout
                print(run_file)
                text_area = script
                input_fields = script_inputs
                output = file_output
    return render_template('index.html',
                           text_area=text_area,
                           input_fields=input_fields,
                           output=output)


if __name__ == "__main__":
    app.run(debug=True)
