public class MyTask implements Runnable {
    public void run() {
        Bukkit.getServer().getConsoleSender().sendMessage("Hello, world!");
    }
}
class MyPlugin extends JavaPlugin {
    private BukkitScheduler scheduler;

    public void onEnable() {
        scheduler = Bukkit.getScheduler();
        scheduler.scheduleSyncRepeatingTask(this, new MyTask(), 0L, 200L);
    }

    public void onDisable() {
        // 停止所有任务
        scheduler.cancelTasks(this);
    }
}