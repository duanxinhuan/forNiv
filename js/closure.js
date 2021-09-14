var counter = ()=>{
    var privateCounter = 0;
    function changeBy(val){
        privateCounter += 1;
    }

    return {
        increment: function(){
            changeBy(1);
        },
        decrement: function(){
            changeBy(-1);
        },
        value: function(){
            return privateCounter
        }
    };
}

var counter1 = counter();
var counter2 = counter();

counter1.increment();
console.log(counter1.value())
console.log(counter2.value())
