import express from 'express';
import { verifyToken } from '../middleware/auth.js';
import UserData from '../models/UserData.js';

const router = express.Router();
router.use(verifyToken);

router.get('/', async (req, res) => {
  const data = await UserData.findOne({ userId: req.userId });
  res.json(data);
});

router.post('/', async (req, res) => {
  const data = await UserData.findOneAndUpdate(
    { userId: req.userId },
    { content: req.body.content },
    { upsert: true, new: true }
  );
  res.json(data);
});

export default router;
