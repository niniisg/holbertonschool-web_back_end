export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof(name) !== 'string') {
            throw TypeError('Name should be a string');
        }
        if (typeof(length) !== 'number') {
            throw TypeError('Length must be a number');
        }

        if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')){
            throw TypeError('Students should be array of string');
        }

        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name(){
        return this._name;
    }
    set name(newName){
        if (typeof(newName) !== 'string'){
            throw TypeError('Name should be a string');
        }
        this._name = newName;
    }
    
    get length(){
        return this._lenght;
    }
    set length(newLenght){
        if (typeof(newLength) !== 'number'){
            throw TypeError('Length must be a number');
        }
        this._length = newLenght;
    }

    get students(){
        return this._students;
    }

    set students(newStudents){
        if (Array.isArray(newStudents) !== true && typeof(newStudents[0] !== 'string')){
            throw TypeError('Students should be array of string');
        }
        this._students = newStudents;
  }
}
