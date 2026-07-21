# TruthLens 部署指南

## 方案一：Vercel（前端）+ Railway（后端）— 推荐

### 前置准备

1. GitHub 账号（https://github.com/signup）
2. Vercel 账号（用 GitHub 登录即可：https://vercel.com/signup）
3. Railway 账号（用 GitHub 登录即可：https://railway.app）

---

## 步骤 1：创建 GitHub 仓库

1. 打开 https://github.com/new
2. Repository name: `truthlens`
3. 选择 **Public**
4. 点击 **Create repository**
5. 复制仓库地址（如 `https://github.com/yourname/truthlens.git`）

---

## 步骤 2：推送代码到 GitHub

在项目根目录执行：

```bash
cd truthlens
git init
git add .
git commit -m "Initial commit: TruthLens for Telegraph Hackathon"
git branch -M main
git remote add origin https://github.com/yourname/truthlens.git
git push -u origin main
```

---

## 步骤 3：部署后端到 Railway

1. 打开 https://railway.app/new
2. 选择 **Deploy from GitHub repo**
3. 选择你的 `truthlens` 仓库
4. Railway 会自动检测 `backend/Dockerfile`，使用 Docker 部署
5. 点击部署，等待完成
6. 部署完成后，Railway 会分配一个公网域名，如 `https://truthlens.up.railway.app`
7. **复制这个域名** — 前端需要用到

### 配置环境变量（Railway）

在 Railway 项目设置中添加环境变量：

| Key | Value |
|-----|-------|
| `TELEGRAPH_DAEMON_URL` | `http://13.237.89.59:7044/daemon` |
| `TELEGRAPH_DISPATCHER_URL` | `http://13.237.89.59:7044/miner-dispatcher` |
| `PAYAI_FACILITATOR_URL` | `https://facilitator.payai.network` |

---

## 步骤 4：修改前端 API 地址

打开 `frontend/.env.local`，将后端的 Railway 域名填入：

```
NEXT_PUBLIC_API_URL=https://truthlens.up.railway.app/api/v1
```

**注意**：把 `truthlens.up.railway.app` 替换为你实际的 Railway 域名。

然后提交修改：

```bash
git add frontend/.env.local
git commit -m "Update API URL for production"
git push
```

---

## 步骤 5：部署前端到 Vercel

1. 打开 https://vercel.com/new
2. 选择你的 `truthlens` GitHub 仓库
3. Vercel 会自动检测 Next.js 项目
4. **重要**：在 Framework Preset 中确认选择了 **Next.js**
5. **Root Directory** 设置为 `frontend`
6. 点击 **Deploy**
7. 等待 1-2 分钟，Vercel 会分配一个域名，如 `https://truthlens.vercel.app`

---

## 完成

- 前端地址：`https://truthlens.vercel.app`
- 后端地址：`https://truthlens.up.railway.app`
- API 文档：`https://truthlens.up.railway.app/docs`

分享前端链接即可让任何人体验 TruthLens。

---

## 方案二：仅部署前端到 Vercel（后端用本地/ngrok）

如果你暂时不想部署后端，可以：

1. 只部署前端到 Vercel（步骤 5）
2. 本地保持后端运行
3. 用 ngrok 暴露本地后端：
   ```bash
   npx ngrok http 8000
   ```
4. 将 ngrok 提供的临时域名填入 `frontend/.env.local`
5. 重新部署前端

**缺点**：ngrok 链接每次重启都会变，且需要保持本地电脑开机。

---

## 方案三：Docker Compose 一键部署（自有服务器）

如果你有云服务器（AWS、阿里云、腾讯云等）：

```bash
git clone https://github.com/yourname/truthlens.git
cd truthlens
docker-compose up -d
```

然后配置 Nginx 反向代理，绑定域名即可。
