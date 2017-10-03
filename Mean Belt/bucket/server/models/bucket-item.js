var mongoose = require('mongoose');
var { Schema } = mongoose;

var bucketItemSchema = new Schema({
  owner: {
    type: Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  completed: {
    type: Boolean,
    default: false
  }
}, { timestamps: true });

mongoose.exports = mongoose.model('BucketItem', bucketItemSchema);
