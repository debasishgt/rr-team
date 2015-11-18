package model;

public class Vehicle {
	private int id;
	private String name;
	private int baseVehicleId;
	private double health;
	private double armor;
	private double weight;
	private double speed;
	private double acceleration;
	private double control;
	
	public Vehicle(int id, String name, int baseVehicleId) {
		this(id,name,0,0.0,0.0,0.0,0.0,0.0,0.0);
	}
	
	public Vehicle(int id, String name, int baseVehicleId, double health, double armor, double weight, double speed, double acceleration, double control) {
		this.id = id;
		this.name = name;
		this.baseVehicleId = baseVehicleId;
		this.health = health;
		this.armor = armor;
		this.weight = weight;
		this.speed = speed;
		this.acceleration = acceleration;
		this.control = control;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public int getBaseVehicleId() {
		return this.baseVehicleId;
	}
	
	public void setBaseVehicleId(int baseVehicleId) {
		this.baseVehicleId = baseVehicleId;
	}

	public double getHealth() {
		return health;
	}

	public void setHealth(double health) {
		this.health = health;
	}

	public double getArmor() {
		return armor;
	}

	public void setArmor(double armor) {
		this.armor = armor;
	}

	public double getWeight() {
		return weight;
	}

	public void setWeight(double weight) {
		this.weight = weight;
	}

	public double getSpeed() {
		return speed;
	}

	public void setSpeed(double speed) {
		this.speed = speed;
	}

	public double getAcceleration() {
		return acceleration;
	}

	public void setAcceleration(double acceleration) {
		this.acceleration = acceleration;
	}

	public double getControl() {
		return control;
	}

	public void setControl(double control) {
		this.control = control;
	}

	public int getId() {
		return id;
	}
}
