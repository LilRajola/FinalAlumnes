extends Area2D


func _on_body_entered(body: Node2D) -> void:
	$SoPowerUP.play()
	body.power_up_bomba()
	hide()


func _on_so_power_up_finished() -> void:
	queue_free()
