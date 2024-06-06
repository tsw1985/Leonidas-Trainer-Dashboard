leonidastrainer.directive("gettrainer", function ($compile) {

    return {
        restrict: 'E',

        template : ' <div class="exerciseResultList"> ' +
                   '<h4 id="titletrainer" class="text-center"></h4>' +
                   '<div id="trainerContent"></div>' +
                   '</div>',

        scope: {
            idtrainer: '='

        },

        controller: function($scope , $http , $compile){

            $scope.alerta = function(idConf, idTrainer){

                console.log("ELIMINANDO " + idConf , idTrainer);
                removeExerciseInTrainer(idConf,idTrainer);

            };

            $scope.$parent.$on('someEvent', function(event, id) {
                loadTrainer(id);
            }); //end parent.on


        function removeExerciseInTrainer(idExerciseConf,idTrainer){
            $http({
                url : '/admin/deleteexercisetotrainer',
                method : 'GET',
                params: {
                         'idConfigurationTrainer'    : idExerciseConf
                        }
            }).success(function(data){

                console.log("ELIMINADO IDCONF " + idExerciseConf );
                loadTrainer(idTrainer);
            });
        }

        function loadTrainer(idTrainer){

             $http({ url : '/admin/gettrainerwithcontent',
                    method : 'GET',
                    params: {
                                'idTrainer' : idTrainer,
                                'idDay'     : 0
                            }
                    }).success(function(data) {

                 if (data.length) {

                     var trainer = data[0].trainer;
                     $("#titletrainer").text(trainer.description);

                     $("#trainerContent").html("");


                     var idTrainer = -1;
                     var totalDays = -1;

                     //angular.forEach(trainer, function(value, key){
                     $.each(data, function (key, value) {

                         $.each(value, function (key2, valueContent) {

                             console.log("VALUE CONTENT");
                             console.log(valueContent);
                             idTrainer = valueContent.id;
                             totalDays = valueContent.totaldays;
                             descriptionTrainer = valueContent.description;
                             console.log("TRAINER ID " + idTrainer + " TOTAL DAYS " + totalDays + " DESC " + descriptionTrainer);

                             var trainerContent = valueContent.content;
                             $.each(trainerContent, function (key2, daysContentValue) {
                                 console.log("TRAINER CONTENT");
                                 console.log(daysContentValue);

                                 //obtenemos los dias
                                 var idDay = daysContentValue.dayId;
                                 var desDay = daysContentValue.dayName;
                                 var bodyPlacesContent = daysContentValue.bodyPlaces;

                                 var divDay = "<div class='dayDiv'  id='day" + idDay + "'>" + desDay + "</div>";
                                 $("#trainerContent").append(divDay);


                                 //recorremos los bodyplaces
                                 $.each(bodyPlacesContent, function (key2, bodyPlaceContentValue) {

                                     var idBodyPlace = bodyPlaceContentValue.id;
                                     var desBodyPlace = bodyPlaceContentValue.name;
                                     var exercices = bodyPlaceContentValue.exercises;


                                     var divBodyPlace = "<div id='bodyplace" + idDay + idBodyPlace + "'  class='bodyPlaceDiv' >" + desBodyPlace + "</div>";
                                     $("#day" + idDay).append(divBodyPlace);

                                     $.each(exercices, function (key3, exercisesValue) {

                                         var exerciseId = exercisesValue.id;
                                         var exerciseLabel = exercisesValue.label;
                                         var idConf = exercisesValue.idconf;

                                         console.log("EXERCISE ID " + exerciseId + " DES EJE " + exerciseLabel);

                                         var button = "<button ng-click=\"alerta(" + idConf + "," + idTrainer  + ")\"  id='exerciseButton'  name='" + idConf + "' class='btn btn-info buttonFloatRight'>-</button>";

                                         var exercisesDiv = "<div  class='exercisesDiv'>" + exerciseLabel + button + "</div>";

                                         //cuando insertamos la etiqueta la compilamos para que reconozca el atrributo ng-click
                                         $("#bodyplace" + idDay + idBodyPlace).append($compile(exercisesDiv)($scope));

                                     });
                                 });
                             });
                         });
                     });

                 }
             });
        }



        } //end controller

    };

});