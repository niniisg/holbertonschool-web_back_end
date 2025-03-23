-- Lists all Glam rock bands, ranked by their longevity
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;