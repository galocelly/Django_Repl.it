angular.module('testService', [])//Declaramos el modulo
	.factory('testRequest', function($http) { //declaramos la factory
		// var path = "http://jsonplaceholder.typicode.com/";//API path
		var path = "http://localhost:8000/";//API path
		return {
			//Login
			posts : function(){ //Retornara la lista de posts
				global = $http.get(path+'snippets');
				return global;
			},
			post : function(id){ //retornara el post por el id
				global = $http.get(path+'snippets/'+id);
				return global;	
			},
      add_post : function(informacion){ //retornara el post por el id
				global = $http.post(path+'snippets/', informacion);
				return global;	
			}	

		}
	});
