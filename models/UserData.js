import mongoose from 'mongoose';

const UserDataSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  content: String,
});

export default mongoose.model('UserData', UserDataSchema);
