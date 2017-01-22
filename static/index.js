TOKEN   = { time_created: 1483449524000,
  msg_mac: 'a/t5W259jFepALUem5WI+hFnYIcoMcW6+ci/kFnPXpA=' }

var repl = new ReplitClient('api.repl.it', '80', 'ruby', TOKEN);

repl.connect().then(
    function() {
        document.querySelector('.status').innerHTML = 'connected';
        start();
    },
    function() {
        document.querySelector('.status').innerHTML = 'failed';
    }
);

function start() {
    document.querySelector('button').onclick = function() {
        repl.evaluate(
            document.querySelector('input').value,
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
