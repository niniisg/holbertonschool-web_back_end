export default class Currency{
    constructor(code, name){
        this._code = code;
        this._name = name;
  
    }
    get code() {
        return this._code;
      }
      set code(newCode) {
        this._code = code
      }
    get name(){
        return this._name;
    }
    set name(newName){
        this._name = newname;
    }

    displayFullCurrency(){
        return `${this._name} ${this._code})`
    }
}



