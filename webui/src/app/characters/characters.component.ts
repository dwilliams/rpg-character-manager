import { Component, OnInit } from '@angular/core';
import { RPGcharacter } from '../rpgcharacter';

@Component({
  selector: 'app-characters',
  templateUrl: './characters.component.html',
  styleUrls: ['./characters.component.css']
})
export class CharactersComponent implements OnInit {
  rpg_character: RPGcharacter = {
    id: 1,
    name: 'Shmoo'
  };

  constructor() { }

  ngOnInit() {
  }

}
