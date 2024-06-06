var leonidastrainer = angular.module('leonidastrainer',['ui.autocomplete','ui.bootstrap']);

//Activamos el CSRF certification
leonidastrainer.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

}]);


//https://github.com/zensh/ui-autocomplete
leonidastrainer.controller('createtrainercontroller' , ['$scope' ,'$http',  function($scope, $http){

    //CreateTrainer structure for database
    $scope.trainerContentArray = { 'trainer' : [] };
    $scope.exercisesInTrainer = [];


    $scope.bodyPlacesArray = { 'bodyplaces' : [] };

    $scope.bodyPlaceSelected = 0;
    $scope.dayTrainerSelected = 0;
    $scope.typeExerciseSelected = 0;
    $scope.trainerSelected = 0;



    $scope.days = [];


    $scope.entrenamiento = "";

    //Get my trainers
    $scope.myTrainers = {
           options: {
               html: true,
               minLength: 1,
               onlySelect: true,
               outHeight: 50,
               source: function (request, response) {

                   $http({
                       url : '/admin/gettrainers',
                       method : 'GET',
                       params: {'find_text' : request.term}
                   }).success(function(data){

                       if (!data.length) {
                           data.push({
                               label: 'not found',
                               value: null,
                               totaldays : 0
                           });
                       }

                       response(data);
                  });
               },
               select : function(event , ui)
               {
                   event.preventDefault();
                   $scope.opciones = ui.item.label + ' ' + ui.item.value;
                   $("#entrenamiento").text(ui.item.label + ' ' + ui.item.value);
                   $scope.trainerSelected = ui.item.item;


                   //ponemos el valor del id entrenamiento al input de al lado
                   //$scope.idtrainerinput = ui.item.item;
                   $scope.$emit('someEvent', $scope.trainerSelected);

                   //console.log("ID " + ui.item.item);
                   //console.log("LABEL " + ui.item.label);
                   //console.log("TOTAL DAYS " + ui.item.totaldays);

                   getDaysForTrainerAndCreateStructureData(ui.item.totaldays);


                     //cargamos los ejercicios si este entrenamiento los tiene
                    //console.log("ID ENTRENAMIENTO A MOSTRAR " + ui.item.item);
                    //getExercisesInTrainer(ui.item.item,$scope.dayTrainerSelected);

               }

           }
    };

     //get my exercices
     $scope.myExercices = {
            options: {
                html: true,
                minLength: 1,
                onlySelect: true,
                outHeight: 50,
                source: function (request, response) {

                    $http({
                        url : '/admin/getexercices',
                        method : 'GET',
                        params: {
                                 'find_text'    : request.term ,
                                 'body_place'   : $scope.bodyPlaceSelected,
                                 'type_exercise': $scope.typeExerciseSelected
                                }

                    }).success(function(data){

                        if (!data.length) {
                            data.push({
                                label: 'not found',
                                value: null,
                                totaldays : 0
                            });
                        }

                        response(data);
                    });
                },
                select : function(event , ui)
                {
                    event.preventDefault();
                    $scope.opciones = ui.item.label + ' ' + ui.item.value;
                    $("#entrenamiento").text(ui.item.label + ' ' + ui.item.value);

                    //console.log("ID " + ui.item.item);
                    //console.log("LABEL " + ui.item.label);
                    //console.log("TOTAL DAYS " + ui.item.totaldays);

                    $scope.days = [];
                    for ( var i = 0 ; i < ui.item.totaldays ; i++){
                        $scope.days.push({'dia':i});
                        //console.log(i);

                    }





                }
            }
     };



    $scope.bodyPlaces = [];
    getBodyPlaces();

    $scope.typeExercises = [];
    getTypeExercises();





    $scope.bodyPlaceClick = function(id){
        $scope.bodyPlaceSelected = id;
        //console.log("SOY CUERPO " + id);
        //console.log("VALOR DAY SELECTED" + $scope.dayTrainerSelected);
    };

    $scope.typeExerciseClick = function(id){
        $scope.typeExerciseSelected = id;
        //console.log("VALOR DAY TYPE EXERCISE " + $scope.typeExerciseSelected);
    };

    $scope.dayClick = function(dia){
        $scope.dayTrainerSelected = dia;
        //console.log("SOY BOTON " + $scope.dayTrainerSelected);
    };


    $scope.addExerciseToTrainer = function(id, description, bodyplace){

        //For DATABASE
        var daySelected =  $scope.dayTrainerSelected;
        var bodyPlaceSelected =  $scope.bodyPlaceSelected;

        var trainer = new Object();
        trainer.idTrainer = $scope.trainerSelected;
        trainer.idExercise = id;
        trainer.idDaySelected = daySelected;
        trainer.idBodyPlaceSelected = bodyPlaceSelected;

        $http.post('/admin/addexercisetotrainer/',{jsonData : angular.toJson(trainer)}
        ).success(function(data, status, headers, config) {
           console.log("GUARDADO");
           //getExercisesInTrainer($scope.trainerSelected,daySelected);
          }).error(function(data, status, headers, config) {
            console.log("ERROR GUARDAR");
          });

        //Llamamos al evento que cargara los datos del entrenamiento
        $scope.$emit('someEvent', $scope.trainerSelected);

    };


    /*
    $scope.removeExerciseToTrainer = function(id){

        $http({
                url : '/admin/deleteexercisetotrainer',
                method : 'GET',
                params: {
                         'idConfigurationTrainer'    : id
                        }

            }).success(function(data){
                getExercisesInTrainer($scope.trainerSelected , $scope.dayTrainerSelected);
            });
        //deleteexercisetotrainer

    };*/



    //funcion que carga los ejercicios dependiendo del filtrado
    $scope.writetext = function(texto){

        if ( texto == ""){
            $scope.exerciseList = [];
        }

        $http({
                url : '/admin/getexercices',
                method : 'GET',
                params: {
                         'find_text'    : texto ,
                         'body_place'   : $scope.bodyPlaceSelected,
                         'type_exercise': $scope.typeExerciseSelected
                        }

            }).success(function(data){

                $scope.exerciseList = [];
                $scope.exerciseList = data;
                //response(data);
            });

    }


    function getDayNameById(id){
        for ( var i = 0 ; i < $scope.trainer_days.length ; i++){
            if ( $scope.trainer_days[i].id = id){
                return $scope.trainer_days[i].name;
            }
        }
    }


    function getBodyPlaceNameById(id){

        for ( var i = 0 ; i < $scope.bodyPlaces.length ; i++){
            if ( $scope.bodyPlaces[i].id = id){
                return $scope.bodyPlaces[i];
            }
        }


    }



    function getBodyPlaces(){

        $http({ url : '/admin/getbodyplaces',
                method : 'GET'
        }).success(function(data){

            if ( data.length ) {
                for (var i = 0; i < data.length; i++) {
                    $scope.bodyPlaces.push({'id': data[i].id , 'label' : data[i].label});


                    //Creamos el objeto para insertarlo en el array de vista
                    var bodyPlaceObject = new Object();
                    bodyPlaceObject[data[i].id] = [];

                    $scope.bodyPlacesArray['bodyplaces'].push(bodyPlaceObject);


                }
            }
      });

        //console.log("ARRAY DE BODY PLACES");
        //console.log($scope.bodyPlacesArray);



    }


    //getconfigurationtrainers
    /*function getExercisesInTrainer(id,day){

        //console.log("Obteniendo ejercicios ID ENTRENAMIENTO " + id);

        $http({ url : '/admin/gettrainerwithcontent',
                method : 'GET',
                params: {
                            'idTrainer' : id,
                            'idDay'     : day
                        }
        }).success(function(data){

            if ( data.length ) {

                //console.log("EJERCICIOS");
                //console.log(data)  ;


                var trainer = data[0].trainer;
                $("#titletrainer").text(trainer.description);


                $("#trainerContent").html("");


                var idTrainer = -1;
                var totalDays = -1;

                //angular.forEach(trainer, function(value, key){
                $.each(data, function(key, value){

                    $.each(value, function(key2, valueContent){

                        console.log("VALUE CONTENT");
                        console.log(valueContent);
                        idTrainer = valueContent.id;
                        totalDays = valueContent.totaldays;
                        descriptionTrainer = valueContent.description;
                        console.log("TRAINER ID " + idTrainer + " TOTAL DAYS " + totalDays + " DESC " + descriptionTrainer);

                        var trainerContent = valueContent.content;
                        $.each(trainerContent, function(key2, daysContentValue){
                            console.log("TRAINER CONTENT");
                            console.log(daysContentValue);

                            //obtenemos los dias
                            var idDay  = daysContentValue.dayId;
                            var desDay = daysContentValue.dayName;
                            var bodyPlacesContent = daysContentValue.bodyPlaces;

                            var divDay = "<div class='dayDiv'  id='day" + idDay + "'>" + desDay + "</div>";
                            $("#trainerContent").append(divDay);


                            //recorremos los bodyplaces
                            $.each(bodyPlacesContent, function(key2, bodyPlaceContentValue){

                                var idBodyPlace  = bodyPlaceContentValue.id;
                                var desBodyPlace = bodyPlaceContentValue.name;
                                var exercices    = bodyPlaceContentValue.exercises;


                                var divBodyPlace = "<div id='bodyplace" + idDay + idBodyPlace +  "'  class='bodyPlaceDiv' >" + desBodyPlace + "</div>";
                                $("#day" + idDay).append(divBodyPlace);

                                $.each(exercices, function(key3, exercisesValue){

                                    var exerciseId    = exercisesValue.id;
                                    var exerciseLabel = exercisesValue.label;
                                    var idConf        = exercisesValue.idconf;

                                    console.log("EXERCISE ID " + exerciseId + " DES EJE " + exerciseLabel );

                                    var button = "<button id='exerciseButton'  name='" + idConf + "' class='btn btn-info buttonFloatRight'>-</button>";

                                    var exercisesDiv = "<div  class='exercisesDiv'>" + exerciseLabel + button + "</div>";
                                    $("#bodyplace" + idDay + idBodyPlace).append(exercisesDiv);

                                });
                            });
                        });
                    });
                });
            }
      });

    }*/

    /*
     $scope.$watch('idtrainerinput' , function(newValue,oldValue){

         $scope.idtrainerinput = newValue;

        //console.log("DESDE CUSTOM DIRECTIVE");
        //console.log("ID TRAINER CUSTOM DIRECTIVE ----- OLD VALUE--" + oldValue + " ----- NEW VALUE ---" + newValue);
     });*/






    function getTypeExercises(){

        $http({ url : '/admin/gettypeexercises',
                method : 'GET'
        }).success(function(data){

            if ( data.length ) {
                for (var i = 0; i < data.length; i++) {
                    $scope.typeExercises.push({'id': data[i].id ,
                                               'label' : data[i].label ,
                                               'bodyPlace' : data[i].bodyPlace
                                               });
                }
            }
        });

    }


    function getDaysForTrainerAndCreateStructureData(limit){

        $http({ url : '/admin/getdays',
                method : 'GET',
                params: {'limit' : limit }
        }).success(function(data){

            if ( data.length ) {

                //$scope.trainer_days = data;
                $scope.trainer_days = [];
                $scope.trainer_days = data;

                //Al cargar los dias generamos el array de la lista de dias
                //y le asignamos un array para cada dia
                for ( var i = 0 ; i < data.length ; i++){

                    var map = new Object();
                    map[data[i].id] = [];
                    $scope.trainerContentArray['trainer'].push(map);

                }
            }

      });
    }

} ]);

