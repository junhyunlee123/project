package com.example.computerBuilderService.api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;

import com.example.computerBuilderService.model.ComputerComponentData;

import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Objects;


@CrossOrigin(origins = "*")

@RestController
@RequestMapping("computerParts/")
public class ComputerPartsController {
    @Autowired
    JdbcTemplate jdbcTemplate;

    @GetMapping(path = "allComponents")
    public ResponseEntity<List<ComputerComponentData>> getAllComponents(){
        List<ComputerComponentData> allComponents = new ArrayList<>(Objects.requireNonNull(getProcessors().getBody()));

        allComponents.addAll(Objects.requireNonNull(getIntelMotherboards().getBody()));
        allComponents.addAll(Objects.requireNonNull(getAmdMotherboards().getBody()));

        allComponents.addAll(Objects.requireNonNull(getMemories().getBody()));

        allComponents.addAll(Objects.requireNonNull(getNvidiaGraphicsCards().getBody()));
        allComponents.addAll(Objects.requireNonNull(getAmdGraphicsCards().getBody()));

        allComponents.addAll(Objects.requireNonNull(getSsdStorages().getBody()));
        allComponents.addAll(Objects.requireNonNull(getHddStorages().getBody()));

        allComponents.addAll(Objects.requireNonNull(getCpuAirCoolerCoolings().getBody()));
        allComponents.addAll(Objects.requireNonNull(getLiquidOrWaterCoolerCoolings().getBody()));

        allComponents.addAll(Objects.requireNonNull(getPowerSupplies().getBody()));

        allComponents.addAll(Objects.requireNonNull(getPCCases().getBody()));

        allComponents.addAll(Objects.requireNonNull(getPCCaseFanCoolings().getBody()));

        return new ResponseEntity<>(allComponents, HttpStatus.OK);
    }


    @GetMapping(path = "processors")
    public ResponseEntity<List<ComputerComponentData>> getProcessors(){
        List<ComputerComponentData> processorsData = jdbcTemplate.query("SELECT * FROM processors", new BeanPropertyRowMapper<>(ComputerComponentData.class));
        return new ResponseEntity<>(processorsData, HttpStatus.OK);
    }

    @GetMapping(path = "processors/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchProcessors(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> processorsData = jdbcTemplate.query("SELECT * FROM processors WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(processorsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "amdMotherboards")
    public ResponseEntity<List<ComputerComponentData>> getAmdMotherboards(){
        try {
            List<ComputerComponentData> amdMotherboardsData = jdbcTemplate.query("SELECT * FROM amdMotherboards", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(amdMotherboardsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }

    }

    @GetMapping(path = "amdMotherboards/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchAmdMotherboards(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> amdMotherboardsData = jdbcTemplate.query("SELECT * FROM amdMotherboards WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(amdMotherboardsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "intelMotherboards")
    public ResponseEntity<List<ComputerComponentData>> getIntelMotherboards(){
        try{
            List<ComputerComponentData> intelMotherboardsData = jdbcTemplate.query("SELECT * FROM intelMotherboards", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(intelMotherboardsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "intelMotherboards/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchIntelMotherboards(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> intelMotherboardsData = jdbcTemplate.query("SELECT * FROM intelMotherboards WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(intelMotherboardsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "amdGraphicsCards")
    public ResponseEntity<List<ComputerComponentData>> getAmdGraphicsCards(){
        try {
            List<ComputerComponentData> amdGraphicsCardsData = jdbcTemplate.query("SELECT * FROM amdGraphicsCards", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(amdGraphicsCardsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "amdGraphicsCards/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchAmdGraphicsCards(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> amdGraphicsCardsData = jdbcTemplate.query("SELECT * FROM amdGraphicsCards WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(amdGraphicsCardsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "nvidiaGraphicsCards")
    public ResponseEntity<List<ComputerComponentData>> getNvidiaGraphicsCards(){
        try {
            List<ComputerComponentData> nvidiaGraphicsCardsData = jdbcTemplate.query("SELECT * FROM nvidiaGraphicsCards", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(nvidiaGraphicsCardsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "nvidiaGraphicsCards/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchNvidiaGraphicsCards(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> nvidiaGraphicsCardsData = jdbcTemplate.query("SELECT * FROM nvidiaGraphicsCards WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(nvidiaGraphicsCardsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "pcCases")
    public ResponseEntity<List<ComputerComponentData>> getPCCases(){
        try {
            List<ComputerComponentData> pcCasesData = jdbcTemplate.query("SELECT * FROM cases", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(pcCasesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "pcCases/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchPCCases(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> pcCasesData = jdbcTemplate.query("SELECT * FROM cases WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(pcCasesData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "memories")
    public ResponseEntity<List<ComputerComponentData>> getMemories(){
        try {
            List<ComputerComponentData> memoriesData = jdbcTemplate.query("SELECT * FROM memories", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(memoriesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "memories/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchMemories(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> memoriesData = jdbcTemplate.query("SELECT * FROM memories WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(memoriesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "hddStorages")
    public ResponseEntity<List<ComputerComponentData>> getHddStorages(){
        try {
            List<ComputerComponentData> hddStoragesData = jdbcTemplate.query("SELECT * FROM hddStorages", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(hddStoragesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "hddStorages/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchHddStorages(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> hddStoragesData = jdbcTemplate.query("SELECT * FROM hddStorages WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(hddStoragesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "ssdStorages")
    public ResponseEntity<List<ComputerComponentData>> getSsdStorages(){
        try {
            List<ComputerComponentData> ssdStoragesData = jdbcTemplate.query("SELECT * FROM ssdStorages", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(ssdStoragesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "ssdStorages/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchSsdStorages(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> ssdStoragesData = jdbcTemplate.query("SELECT * FROM ssdStorages WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(ssdStoragesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "powerSupplies")
    public ResponseEntity<List<ComputerComponentData>> getPowerSupplies(){
        try {
            List<ComputerComponentData> powerSuppliesData = jdbcTemplate.query("SELECT * FROM powerSupplies", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(powerSuppliesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "powerSupplies/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchPowerSupplies(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> powerSuppliesData = jdbcTemplate.query("SELECT * FROM powerSupplies WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(powerSuppliesData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "cpuAirCoolerCoolings")
    public ResponseEntity<List<ComputerComponentData>> getCpuAirCoolerCoolings(){
        try {
            List<ComputerComponentData> cpuAirCoolerCoolingsData = jdbcTemplate.query("SELECT * FROM cpuAirCoolerCoolings", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(cpuAirCoolerCoolingsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "cpuAirCoolerCoolings/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchCpuAirCoolerCoolings(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> cpuAirCoolerCoolingsData = jdbcTemplate.query("SELECT * FROM cpuAirCoolerCoolings WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(cpuAirCoolerCoolingsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "liquidOrWaterCoolerCoolings")
    public ResponseEntity<List<ComputerComponentData>> getLiquidOrWaterCoolerCoolings(){
        try {
            List<ComputerComponentData> liquidOrWaterCoolerCoolingsData = jdbcTemplate.query("SELECT * FROM liquidOrWaterCoolerCoolings", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(liquidOrWaterCoolerCoolingsData, HttpStatus.OK);
        } catch (Exception exception) {
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "liquidOrWaterCoolerCoolings/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchLiquidOrWaterCoolerCoolings(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> liquidOrWaterCoolerCoolingsData = jdbcTemplate.query("SELECT * FROM liquidOrWaterCoolerCoolings WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(liquidOrWaterCoolerCoolingsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping(path = "pcCaseFanCoolings")
    public ResponseEntity<List<ComputerComponentData>> getPCCaseFanCoolings(){
        try {
            List<ComputerComponentData> pcCaseFanCoolingsData = jdbcTemplate.query("SELECT * FROM pcCaseFanCoolings", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(pcCaseFanCoolingsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(path = "pcCaseFanCoolings/{keyword}")
    public ResponseEntity<List<ComputerComponentData>> searchPcCaseFanCoolings(@Valid @NotBlank @PathVariable("keyword") String searchKeyword){
        try {
            List<ComputerComponentData> pcCaseFanCoolingsData = jdbcTemplate.query("SELECT * FROM pcCaseFanCoolings WHERE productName LIKE \"%" + searchKeyword.substring(1, searchKeyword.length()).toLowerCase(Locale.ROOT) + "%\"", new BeanPropertyRowMapper<>(ComputerComponentData.class));
            return new ResponseEntity<>(pcCaseFanCoolingsData, HttpStatus.OK);
        } catch (Exception exception){
            System.out.println("Exception Occurred during querying data from database");
            return new ResponseEntity<>(null, HttpStatus.BAD_REQUEST);
        }
    }
}
