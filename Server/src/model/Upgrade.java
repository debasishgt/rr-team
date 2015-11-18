package model;

public class Upgrade {
	private int id;
	private String name;
	private String description;
	private double armor;
	private double health;
	private double acceleration;
	
	public Upgrade(int id, String name) {
		this(id,name,"",0.0,0.0,0.0);
	}
	
	public Upgrade(int id, String name, String description, double armor, double health, double acceleration) {
		this.id = id;
		this.name = name;
		this.description = description;
		this.armor = armor;
		this.health = health;
		this.acceleration = acceleration;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public double getArmor() {
		return armor;
	}

	public void setArmor(double armor) {
		this.armor = armor;
	}

	public double getHealth() {
		return health;
	}

	public void setHealth(double health) {
		this.health = health;
	}

	public double getAcceleration() {
		return acceleration;
	}

	public void setAcceleration(double acceleration) {
		this.acceleration = acceleration;
	}

	public int getId() {
		return id;
	}
}
