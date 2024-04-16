from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        
            
        sepal_length = request.form['sepalLength']
        sepal_width = request.form['sepalWidth']
        petal_length = request.form['petalLength']
        petal_width = request.form['petalWidth']
        
        
        # # this is my final data
        # final_data=data.get_data_as_dataframe()
        
        # predict_pipeline=PredictPipeline()
        
        # pred=predict_pipeline.predict(final_data)
        
        # result=round(pred[0],2)
        
        return render_template("submission.html")



if __name__ == '__main__':
    app.run(debug=True)
