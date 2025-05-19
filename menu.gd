extends Node2D

func _on_jugar_pressed() -> void:
	get_tree().change_scene_to_file("res://Escenes/joc.tscn")

func _on_adeu_pressed() -> void:
	_exit_tree()
