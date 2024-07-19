export default class Building {
  constructor(sqft) {
    if (this._constructer !== Building && !this.evacuationWariningMessage) {
      throw TypeError('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
