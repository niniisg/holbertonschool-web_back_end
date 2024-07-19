export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof(name) !== 'string') {
            throw TypeError('name should be a string');
        }
        if (typeof(length) !== 'number') {
            throw TypeError('must be a Number');
        }

        if (Array.isArray(students) !== true && typeof(students[0] !== 'string')){
            throw TypeError('students should be array of string');
        }

        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name(){
        return this._name;
    }
    set name(name){
        if (typeof(name) !== 'string'){
            throw TypeError('name should be a string');
        }
        this._name = name;
    }
    
    get length(){
        return this._lenght;
    }
    set length(lenght){
        if (typeof(length) !== 'lenght'){
            throw TypeError('must be a Number');
        }
        this._length = lenght;
    }

    get students(){
        return this._students;
    }

    set students(students){
        if (Array.isArray(students) !== true && typeof(students[0] !== 'string')){
            throw TypeError('students should be array of string');
        }
        this._students = students;
  }
}
