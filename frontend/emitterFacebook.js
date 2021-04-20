/*
 * [Facebook description]
 * Create an event emitter that goes like this
 * emitter = new Emitter();
 *
 * Allows you to subscribe to some event
 * sub1 = emitter.subscribe('function_name', callback1);
 * (you can have multiple callbacks to the same event)
 * sub2 = emitter.subscribe('function_name', callback2);
 *
 * You can emit the event you want with this api
 * (you can receive 'n' number of arguments)
 * sub1.emit('function_name', foo, bar);
 *
 * And allows you to release the subscription like this
 * (but you should be able to still emit from sub2)
 * sub1.release();
 */

class Emitter {
  constructor(events = {}) {
    this.events = events;
  }

  subscribe(name, callback) {
    if (!(name in this.events))
      this.events[name] = [callback]
    else
      this.events.push(callback);
    return {
      name,
      callback,
      release: () => this.delete(name, callback),
    }
  }

  emit(name, ...args) {
    if (name in this.events)
      this.events[name].forEach(fn => fn(...args));
    else
      console.log("this event is not registered!")
  }

  delete(name, callback) {
    this.events[name] = this.events[name].filter((fn) => fn != callback);
  }
}

let emitter = new Emitter();
let callback1 = (...args) => console.log(...args)
let callback2 = () => console.log("callback2")
sub1 = emitter.subscribe('function_1', callback1);
sub2 = emitter.subscribe('function_2', callback2);
emitter.emit('function_1', 'hey', 'wassup', 'what');
emitter.emit('function_2');
sub1.release();
emitter.emit('function_1');
emitter.emit('function_2');