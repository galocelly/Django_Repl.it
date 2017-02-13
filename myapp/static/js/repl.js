
     TOKEN   = { time_created: 1486919221000,
  msg_mac: 'bqusctfzUcaQ7M+SAreyuiiWS0sUiC8XST3H98yZeQ4='}

        var repl = new ReplitClient('api.repl.it', '80', 'java', TOKEN);

        repl.connect().then(
            function() {
                document.querySelector('.status').innerHTML = 'OK';
                start();
            },
            function() {
                document.querySelector('.status').innerHTML = 'FALLO';
            }
        );

        function start() {
            document.querySelector('#run').onclick = function() {
                repl.evaluate(
                    document.querySelector('#id_code').value,
                     {    
                        stdout: function(str) {
                            document.querySelector('.out').innerHTML += str + '\n';
                        }
                     }
                ).then(
                    function(result) {
                        document.querySelector('.result').innerHTML += (result.error || result.data) + '\n';
                    },
                    function(err) {
                        console.error(err);
                    }
                );
            };
        }




