# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T16:11:33+00:00

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class BasicModelStats(BaseModel):
    average: float = Field(..., title='Average')
    median: float = Field(..., title='Median')
    name: str = Field(..., title='Name')
    pVariance: float = Field(..., title='Pvariance')
    stdDev: float = Field(..., title='Stddev')


class BasicModelStatsResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[BasicModelStats] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class BooleanResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: bool = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class BrandResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[str] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class BucketEntry(BaseModel):
    bucket: float = Field(..., title='Bucket')
    modelName: str = Field(..., title='Modelname')
    percentOfMarket: float = Field(..., title='Percentofmarket')


class BucketResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[BucketEntry] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class DealershipData(BaseModel):
    address: str = Field(..., title='Address')
    dealerName: str = Field(..., title='Dealername')
    ids: List[int] = Field(..., title='Ids')
    state: str = Field(..., title='State')
    zipCode: int = Field(..., title='Zipcode')


class DealershipDataPaginated(BaseModel):
    dealers: List[DealershipData] = Field(..., title='Dealers')
    maxPages: int = Field(..., title='Maxpages')
    page: int = Field(..., title='Page')


class DealershipDataPaginatedResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: DealershipDataPaginated
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class DealershipDataResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[DealershipData] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class EndpointList(BaseModel):
    endPoints: Optional[List[str]] = Field(['*'], title='Endpoints')


class GenericResponse(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: Optional[Any] = Field(None, title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class JSONWebToken(BaseModel):
    createdOn: Optional[int] = Field(None, title='Createdon')
    expires: Optional[int] = Field(None, title='Expires')
    token: str = Field(..., title='Token')


class Listing(BaseModel):
    askPrice: float = Field(..., title='Askprice')
    brandName: str = Field(..., title='Brandname')
    color: Optional[str] = Field(None, title='Color')
    dealerID: int = Field(..., title='Dealerid')
    firstSeen: date = Field(..., title='Firstseen')
    interiorColor: Optional[str] = Field(None, title='Interiorcolor')
    isNew: bool = Field(..., title='Isnew')
    lastSeen: date = Field(..., title='Lastseen')
    mileage: Optional[float] = Field(0, title='Mileage')
    modelName: str = Field(..., title='Modelname')
    msrp: float = Field(..., title='Msrp')
    vin: str = Field(..., title='Vin')
    vinDecode: Optional[Dict[str, Any]] = Field({}, title='Vindecode')
    year: float = Field(..., title='Year')


class ListingRespPaginated(BaseModel):
    listings: List[Listing] = Field(..., title='Listings')
    maxPages: int = Field(..., title='Maxpages')
    page: int = Field(..., title='Page')


class ModelDict(BaseModel):
    modelName: str = Field(..., title='Modelname')


class ModelResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[ModelDict] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class ModelYearDistEntry(BaseModel):
    brandName: str = Field(..., title='Brandname')
    modelName: str = Field(..., title='Modelname')
    percentOfMarket: float = Field(..., title='Percentofmarket')
    year: int = Field(..., title='Year')


class ModelYearDistResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[ModelYearDistEntry] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class RegionResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[str] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class SimilarSalePriceData(BaseModel):
    daysBack: int = Field(..., title='Daysback')
    mileCount: int = Field(..., title='Milecount')
    milesAvg: float = Field(..., title='Milesavg')
    milesStdDev: float = Field(..., title='Milesstddev')
    newCount: int = Field(..., title='Newcount')
    newSaleAvg: float = Field(..., title='Newsaleavg')
    newSaleStdDev: float = Field(..., title='Newsalestddev')
    usedCount: int = Field(..., title='Usedcount')
    usedSaleAvg: float = Field(..., title='Usedsaleavg')
    usedSaleStdDev: float = Field(..., title='Usedsalestddev')


class SimilarSalePriceResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: SimilarSalePriceData
    endDate: date = Field(..., title='Enddate')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')
    startDate: date = Field(..., title='Startdate')


class SubUserJSONWebToken(BaseModel):
    createdOn: Optional[int] = Field(None, title='Createdon')
    domain: str = Field(..., title='Domain')
    endPoints: Optional[List[str]] = Field(['*'], title='Endpoints')
    expires: Optional[int] = Field(None, title='Expires')
    token: str = Field(..., title='Token')
    uuid: str = Field(..., title='Uuid')


class TopModelEntry(BaseModel):
    brandMarketShare: float = Field(..., title='Brandmarketshare')
    brandName: str = Field(..., title='Brandname')
    modelName: str = Field(..., title='Modelname')
    percentOfBrandSales: float = Field(..., title='Percentofbrandsales')
    percentOfTopSales: float = Field(..., title='Percentoftopsales')


class TopModelResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: List[TopModelEntry] = Field(..., title='Data')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VehHistory(BaseModel):
    dealerName: str = Field(..., title='Dealername')
    firstSeen: date = Field(..., title='Firstseen')
    lastSeen: date = Field(..., title='Lastseen')
    miles: int = Field(..., title='Miles')
    new: bool = Field(..., title='New')
    price: float = Field(..., title='Price')
    state: str = Field(..., title='State')
    zip: int = Field(..., title='Zip')


class VehHistoryData(BaseModel):
    data: List[VehHistory] = Field(..., title='Data')
    vin: str = Field(..., title='Vin')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class HistoryResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: VehHistoryData
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')


class ListingResp(BaseModel):
    brandName: Optional[str] = Field(None, title='Brandname')
    cacheTimeLimit: Optional[int] = Field(600, title='Cachetimelimit')
    condition: Optional[str] = Field(None, title='Condition')
    data: ListingRespPaginated
    endDate: Optional[date] = Field(None, title='Enddate')
    modelName: Optional[str] = Field(None, title='Modelname')
    msg: Optional[str] = Field(None, title='Msg')
    regionName: Optional[str] = Field(None, title='Regionname')
    startDate: Optional[date] = Field(None, title='Startdate')
