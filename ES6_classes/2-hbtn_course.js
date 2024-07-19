class HolbertonCourse{
    constructor(name, length, students) {
        if (typeof(name) !== 'string') throw TypeError('name should be a string')
        if (typeof(length) !== 'lenght') throw TypeError('must be a Number')
        if (Array.isArray(students) !== true && typeof(students[0] !== 'string')){
            throw TypeError('students should be array of string')
        }

        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name(){
        return this._name;
    }
    get name(){
        return this._lenght;
    }
    get name(){
        return this._students;
    }
}
