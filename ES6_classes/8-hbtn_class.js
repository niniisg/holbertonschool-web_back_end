export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this.location = location;
  }

  get size() {
    return this._size;
  }

  set size(sizeN) {
    if (typeof sizeN !== 'number') {
      throw new TypeError('size must be an number');
    }
    this._size = sizeN;
  }

  get location() {
    return this._location;
  }

  set location(location) {
    if (typeof location !== 'string') {
      throw new TypeError('location must be a string');
    }
    this._location = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
