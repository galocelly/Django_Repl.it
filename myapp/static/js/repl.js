     TOKEN   = { time_created: 1485633510000,
  msg_mac: '6Hnee1n5d0ioC1UoUDjBA3JJfz3r5eJKpgME18r6j08='}

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




