function User(data) {
    this.id = ko.observable(data.id);
    this.full_name = ko.observable(data.full_name);
    this.username = ko.observable(data.username);
    this.emailid = ko.observable(data.emailid);
    this.password = ko.observable(data.password);
}

function UserListViewModel() {
    var self = this;
    self.user_list = ko.observableArray([]);
    self.full_name = ko.observable();
    self.username= ko.observable();
    self.emailid= ko.observable();
    self.password= ko.observable();

    self.addUser = function() {
	self.save();
  self.full_name("");
	self.username("");
	self.emailid("");
  self.password("");
    };

    $.getJSON('/api/v1/users', function(userModels) {
	var t = $.map(userModels.user_list, function(item) {
	    return new User(item);
	});
	self.user_list(t);
    });

    self.save = function() {
	return $.ajax({
	    url: '/api/v1/users',
	    contentType: 'application/json',
	    type: 'POST',
	    data: JSON.stringify({
		'full_name': self.full_name(),
		'username': self.username(),
        'emailid': self.emailid(),
        'password': self.password()
	    }),
	    success: function(data) {
          alert("success")
		      console.log("Pushing to users array");
		      self.push(new User({ full_name: data.full_name, username: data.username,emailid: data.emailid ,password: data.password}));
		      return;
	    },
	    error: function() {
		return console.log("Failed");
	    }
	});
    };
}

ko.applyBindings(new UserListViewModel());