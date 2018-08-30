from __future__ import print_function
from string import Template

def lambda_html_handler(event, context):
    html = """
                <html>
                  <head>
                    <title>Simple SAM based Contact Form</title>
                      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
                      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>                    
                  </head>
                  <body>
                    <div class="col-md-6">
                    <h2>Simple SAM based Contact Form</h2>  
                      <form action="%TODO%" method=post>
                        <div class="form-group">
                          <label for="name">Name:</label>
                          <input type="text" class="form-control" name="name">
                        </div>
                        <div class="form-group">
                          <label for="message">Message:</label>
                          <textarea class="form-control" name="message" rows="3"></textarea>
                        </div>
                        <button type="submit" class="btn btn-default">Submit</button>
                      </form>                     
                    </div>
    </body></html>
    """

    return {
        "statusCode": 200,
        "headers": {
          "Content-Type": "text/html"          
        },
        "body": html
    }    