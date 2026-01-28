"""Класс статуса заказа"""
import enum

class OrderStatus(enum.StrEnum):
    NEW = 'Новый'
    PREPARING = 'Готовится'
    READY = 'Готов'