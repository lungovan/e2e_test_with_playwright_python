pipeline {
    agent any
	parameters {
        choice(choices: ['Release'], description: 'Please choose the build configuration?', name: 'configuration')
    }

    stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
		stage('Install dependencies') {
			steps {
				script {
					echo "Installing dependencies..."
					sh "cd ${WORKSPACE}; python3 -m venv ${WORKSPACE}/venv"
					sh "cd ${WORKSPACE}; ${WORKSPACE}/venv/bin/python -m pip install --upgrade pip"
					sh "cd ${WORKSPACE}; ${WORKSPACE}/venv/bin/pip install -r requirements.txt"
					sh "cd ${WORKSPACE};  ${WORKSPACE}/venv/bin/python -m playwright install --with-deps"
				}
			}
		}
		stage('Run test') {
			steps{
				script {
                    sh "cd ${WORKSPACE};  pytest"
				}
			}
		}
	}
	 post {
        always
		{
            echo 'Sending mail - post build!'
            emailext attachLog: true,
					 body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} \n More info at: ${env.BUILD_URL}",
					 subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
					 to : "lungovan@gmail.com"
		}
    }
}