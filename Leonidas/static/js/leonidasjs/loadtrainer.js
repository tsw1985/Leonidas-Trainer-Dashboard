/*$(document).ready(function(){

    $(document).on("click", "button#exerciseButton", function() {
        var id = $(this).attr('name');
        console.log("ID EJERCICIO " + id);
        alert("ID " + id);

        getExercisesInTrainer(1,1);

    });


    //getconfigurationtrainers
    function getExercisesInTrainer(id,day){

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

    }



});
*/