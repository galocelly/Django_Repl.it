angular.module('testService', [])//Declaramos el modulo
	.factory('testRequest', function($http) { //declaramos la factory
		// var path = "http://jsonplaceholder.typicode.com/";//API path
		var path = "http://localhost:8000/";//API path
		return {
			//Login
			posts : function(){ //Retornara la lista de posts
				global = $http.get(path+'snippets/');
				return global;
			},
			post : function(id){ //retornara el post por el id
				global = $http.get(path+'snippets/'+id+'/');
				return global;	
			},
      add_post : function(informacion){ //retornara el post por el id
				global = $http.post(path+'snippets/', informacion);
				return global;	
			},	

			del_post : function(id){ //retornara el post por el id
				console.log ("delete");
				global = $http.delete(path+'snippets/'+id+'/');
				return global;	
			},
			put_post : function(id, informacion){ //retornara el post por el id
				console.log (informacion);
				console.log (id);
				global = $http.put(path+'snippets/'+id+'/', informacion);
				return global;	
			},	
			postslen : function(){ //Retornara la lista de posts
				global = $http.get(path+'tipo/');
				return global;
			},

postslenn : function(id){ //Retornara la lista de posts
				global = $http.get(path+'tipo/'+id+'/');
				return global;
			}
		}
	});
