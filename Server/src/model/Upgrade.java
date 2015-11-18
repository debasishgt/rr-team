package model;

public class Upgrade {
	private int id;
	private String name;
	private String description;
	private double damage;
	private double armor;
	private double health;
	private double acceleration;
	private boolean can_make_immune;
	private boolean can_blind;
	private boolean can_toggle;
	
	public Upgrade(int id, String name) {
		this(id,name,"",0.0,0.0,0.0,0.0,false,false,false);
	}
	
	public Upgrade(int id, String name, String description, double damage, double armor, double health, double acceleration, boolean canMakeImmune, boolean canBlind, boolean canToggle) {
		this.id = id;
		this.name = name;
		this.description = description;
		this.damage = damage;
		this.armor = armor;
		this.health = health;
		this.acceleration = acceleration;
		this.can_make_immune = canMakeImmune;
		this.can_blind = canBlind;
		this.can_toggle = canToggle;
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

	public double getDamage() {
		return damage;
	}

	public void setDamage(double damage) {
		this.damage = damage;
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

	public boolean isCanMakeImmune() {
		return can_make_immune;
	}

	public void setCanMakeImmune(boolean canMakeImmune) {
		this.can_make_immune = canMakeImmune;
	}

	public boolean isCanBlind() {
		return can_blind;
	}

	public void setCanBlind(boolean canBlind) {
		this.can_blind = canBlind;
	}

	public boolean isCanToggle() {
		return can_toggle;
	}

	public void setCanToggle(boolean canToggle) {
		this.can_toggle = canToggle;
	}

	public int getId() {
		return id;
	}
}
