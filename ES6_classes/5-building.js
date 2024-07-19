export default class Building {
  constructor(sqft) {
    if (this.constructer !== Building && !this.evacuationWariningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
