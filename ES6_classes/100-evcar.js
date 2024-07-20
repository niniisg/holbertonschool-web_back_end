import Car from './10-car';
export default class EVCar extends Car {
    constructor(brand, motor,color,ranger){
        this._brand = brand;
        this._motor = motor;
        this._color = color;
        this._ranger = ranger;

    }
    cloneCar(){
        return new Car;
    }

}