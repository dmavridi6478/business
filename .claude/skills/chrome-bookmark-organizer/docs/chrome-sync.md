# Chrome Sync 与本地书签编辑

## TL;DR

如果你的 Chrome 登录了 Google 账号 **且**开启了书签同步，**直接编辑 `Bookmarks` JSON 文件的修改会在 Chrome 启动时被云端版本覆盖**。

正确流程：
1. 关同步 → 2. 关 Chrome → 3. 改文件 → 4. 开 Chrome（验收）→ 5. 开同步并选"合并本地数据"

## 为什么会被覆盖

Chrome Sync 是双向同步，但冲突解决偏向云端。每个书签节点有 server-side 时间戳和 hash。当你在外部编辑文件：

- **本地新增文件夹**：云端没有这个节点 → 被识别为"本地新增" → push 到云端 ✓
- **本地修改已有节点的位置**（移动到别的文件夹）：云端的版本时间戳更新 → 本地被覆盖 ✗
- **本地删除已有节点**：云端仍有这个节点 → 被恢复 ✗

这就是为什么外部编辑后看到的现象通常是：你新建的空文件夹保留了，但里面应该归类的项目都退回了原位。

## 怎么干净地编辑

### 方案 A：手动开关同步（推荐）

1. 在 Chrome 里打开 `chrome://settings/syncSetup`
2. 点击 **"关闭"**（Turn off）按钮
3. 完全退出 Chrome（macOS：⌘+Q；Windows：右键托盘退出）
4. 用脚本/工具修改 `Bookmarks` 文件
5. 重新打开 Chrome，验收结构
6. 重新开启同步：`chrome://settings/syncSetup` → 登录账号
7. Chrome 会问"如何处理本地与云端数据"——选 **"合并我的数据"** 或 **"保留本地"**，**不要**选"使用云端"

### 方案 B：完全不开同步

如果你不依赖 Chrome 跨设备同步书签，最简单的就是不开同步。`chrome://settings/syncSetup` → 关闭即可。

### 方案 C：用 Chrome 扩展 / 书签 API（最干净，但需要装扩展）

写一个 Chrome 扩展，调用 `chrome.bookmarks.move()`、`chrome.bookmarks.create()` 等 API。这是 Chrome 自己的接口，所有改动会被同步引擎正确识别为本地修改并 push 到云端。

本仓库的 `extension/` 目录是这个方向的占位（尚未实现）。

## 怎么判断同步是开着的

```bash
# macOS
python3 -c "
import json
with open('${HOME}/Library/Application Support/Google/Chrome/Local State') as f:
    ls = json.load(f)
for name, info in ls.get('profile', {}).get('info_cache', {}).items():
    print(f'{name}: user_name={info.get(\"user_name\", \"(none)\")}')"
```

如果某个 profile 的 `user_name` 不是空字符串，说明它登录了 Google 账号，**很可能**同步在跑（同步可以单独关，但默认是开的）。

更直接的判断：看 `Sync Data/` 目录的最近修改时间，如果是最近几分钟内 Chrome 在跑期间被更新，就是开着的。

## 应急回滚

如果改坏了：

```bash
# 找到时间戳备份
ls ~/Library/Application\ Support/Google/Chrome/Default/Bookmarks.backup-*

# Chrome 必须关闭！
cp ~/Library/Application\ Support/Google/Chrome/Default/Bookmarks.backup-<timestamp> \
   ~/Library/Application\ Support/Google/Chrome/Default/Bookmarks
```

如果同步是开的且已经把坏数据推到了云端：去 [chrome.google.com/sync](https://chrome.google.com/sync) 可以重置云端数据，然后从备份恢复本地后再开同步。
