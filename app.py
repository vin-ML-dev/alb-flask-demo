from flask import Flask

app = Flask(__name__)

# Root route
#@app.route('/')
@app.route('/')
def home():
    return "Welcome to EKS Application Loadbalancer Controller example"

# Route for /app1
@app.route('/app1')
def app1():
    return "Welcome to app1"

# Route for /app2
@app.route('/app2')
def app2():
    return "Welcome to app2"

# Custom health check route for ALB
@app.route('/check-health')
def health_check():
    # You can return a simple plain text or HTML response indicating the service is healthy.
    return "Health check passed", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
