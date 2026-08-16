"""Matching test file for wishlist.SOLUTION.py."""
from app.cart import Cart
from solutions.wishlist_SOLUTION import Wishlist, move_to_cart  # adjust import to your module path


def test_add_and_contains():
    w = Wishlist("u1")
    w.add("SKU1")
    assert w.contains("SKU1")


def test_move_to_cart_success():
    w = Wishlist("u1")
    w.add("SKU1")
    cart = Cart()
    err = move_to_cart(w, "SKU1", cart, unit_price=9.99, quantity=2)
    assert err is None
    assert cart.total() == 19.98
    assert not w.contains("SKU1")


def test_move_to_cart_not_in_wishlist():
    w = Wishlist("u1")
    cart = Cart()
    err = move_to_cart(w, "SKU_MISSING", cart, unit_price=5.0)
    assert err is not None
    assert cart.total() == 0
