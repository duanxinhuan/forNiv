var Person = function(name) {
    this.name = name;
    this.canTalk = true;
  };
  
Person.prototype.greet = function() {
    if (this.canTalk) {
        console.log('Hi, I am ' + this.name);
    }
};

var Employee = function(name, title) {
    Person.call(this, name);
    this.title = title;
  };
  
Employee.prototype = Object.create(Person.prototype);
Employee.prototype.constructor = Employee; 

var bob = new Employee('Bob', 'Builder');
bob.greet()