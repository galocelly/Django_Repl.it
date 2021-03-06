angular.module('myApp', ['testService']);

angular.module('myApp').controller('testController', ['$scope','testRequest',testController]);
function testController($scope, testRequest) {
	$scope.posts={};
	$scope.mensaje="";
	$scope.getAllCodes = function(){
		testRequest.posts().then(function (data){
      console.log("...");
      console.log(data.data);
			$scope.posts=data.data; // Asignaremos los datos de todos los posts
			$scope.posts.exist=1;
		});
	}
	$scope.getCodes = function(){
		$scope.unPost={};
		testRequest.post($scope.post_id).then(function (data){
			$scope.unPost=data.data; // Asignaremos los datos del post
			$scope.unPost.exist=1;
			$scope.posts.exist=0;
		});
	}

	$scope.getTipo = function(){
		$scope.unPostipo={};
		testRequest.post($scope.post_id).then(function (data){
			$scope.unPostipo=data.data; // Asignaremos los datos del post
			$scope.unPostipo.exist=1;
			$scope.post.exist=0;
		});
	}
  $scope.crear = function(){
    datos = {'id_code': $scope.a.id_code, 'user': $scope.a.user, 'code': $scope.a.code, 'nombre_codigo': $scope.a.nombre_codigo, 'referencia': $scope.a.referencia, 'idtipo':$scope.a.idtipo}
		testRequest.add_post(datos).then(function (data){
			$scope.mensaje=data.status; // Asignaremos los datos del post
      console.log(data);
		});
	}


	$scope.deletecod = function(){
		console.log($scope.post_id_delete);
		$scope.unPostdel={};
		testRequest.del_post($scope.post_id_delete);//{

	}

	  $scope.actualizar = function(){
    datos = {'id_code': $scope.unPost.id_code, 'user': $scope.unPost.user, 'code': $scope.unPost.code, 'nombre_codigo': $scope.unPost.nombre_codigo, 'referencia': $scope.unPost.referencia, 'idtipo':$scope.unPost.idtipo}
		testRequest.put_post($scope.unPost.id_code, datos).then(function(data){
			$scope.mensaje=data.status; // Asignaremos los datos del post
      		console.log(data);
		});
	}

	// $scope.getAllLenguajes= function(){
		testRequest.postslen().then(function (data){
      console.log("...");
      console.log(data.data);
			$scope.postslen=data.data; // Asignaremos los datos de todos los posts
			$scope.postslen.exist=1;
		});
			
}





		
