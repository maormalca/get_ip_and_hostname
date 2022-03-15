node("maorsslave"){

    dir("${env.BUILD_NUMBER}"){
    stage("git clone"){
        sh 'git clone https://github.com/maormalca/get_ip_and_hostname.git'
    }
    dir ("get_ip_and_hostname"){
        stage("build and deploy"){
            sh "sudo docker-compose up -d"
        }
    }
    stage("test"){
        def test = sh(returnStdout: true, script: 'curl localhost:8087 &> /dev/null && echo $?').trim() 
        if (test != '0' ){
        error("Build failed webserver is down..")
        }
        else{
            println("suscessful")
            }
    }
    }
}

