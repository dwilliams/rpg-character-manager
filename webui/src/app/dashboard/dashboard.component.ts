import { Component, OnInit } from '@angular/core';
import { RPGcharacter } from '../rpgcharacter';
import { CharacterService } from '../character.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  characters: RPGcharacter[] = [];

  constructor(private characterService: CharacterService) { }

  ngOnInit() {
    this.getCharacters();
  }

  getCharacters(): void {
    this.characterService.getCharacters().subscribe(characters => this.characters = characters.slice(1, 5));
  }
}
