const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  preferences: { type: Object, default: {} }
});

module.exports = mongoose.model('User', userSchema);
