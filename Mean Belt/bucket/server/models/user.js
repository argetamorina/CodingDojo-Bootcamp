var mongoose = require('mongoose');
var { Schema } = mongoose;

var userSchema = new Schema({
  name: {
    type: String,
    unique: true,
    required: true
  },
  bucket_items: [{
    type: Schema.Types.ObjectId,
    ref: 'BucketItem'
  }]
});

mongoose.exports = mongoose.model('User', userSchema);
